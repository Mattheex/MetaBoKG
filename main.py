import os
from anyio import open_file
from openai import OpenAI
import pandas as pd
import glob
from matchms.importing import load_from_mgf
from matchms.filtering import add_precursor_mz
from matchms.filtering import normalize_intensities
from matchms.filtering import reduce_to_number_of_peaks
from spec2vec import SpectrumDocument
from rdflib.namespace import RDF, RDFS, XSD, FOAF
from rdflib import Graph, Namespace, term
from random import random
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)


def read_data():
    quant_path = glob.glob("*.mgf")[0]
    quant_table = pd.read_csv(quant_path, sep=",")

    return quant_table


def load_and_filter_from_mgf(path) -> list:
    """Load and filter spectra from mgf file
    Returns:
        spectrums (list of matchms.spectrum): a list of matchms.spectrum objects
    """

    def apply_filters(spectrum):
        spectrum = add_precursor_mz(spectrum)
        spectrum = normalize_intensities(spectrum)
        spectrum = reduce_to_number_of_peaks(spectrum, n_required=1, n_max=100)
        spectrum = add_precursor_mz(spectrum)
        # print(spectrum)
        # spectrum = add_losses(spectrum, loss_mz_from=10, loss_mz_to=200) Directly from spectrum `spectrum.compute_losses(loss_mz_from, loss_mz_to)`
        return spectrum

    spectra_list = [apply_filters(s) for s in load_from_mgf(glob.glob(path)[0])]
    spectra_list = [s for s in spectra_list if s is not None]
    return spectra_list


def classic():
    kg_uri = "https://enpkg.commons-lab.org/kg/"
    ns_kg = Namespace(kg_uri)
    prefix = "enpkg"
    g = Graph()
    g.bind(prefix, ns_kg)
    g.add((ns_kg[feature_id], ns_kg.has_spec2vec_doc, document_id))
    g.add((ns_kg[document_id], RDF.type, ns_kg.Spec2VecDoc))
    g.add((ns_kg[document_id], RDFS.label, term.Literal(f"Spec2vec document {usi}")))
    g.serialize(destination="schema.ttl", format="ttl", encoding="utf-8")


kg_uri = "https://enpkg.commons-lab.org/kg/"
ns_kg = Namespace(kg_uri)
prefix = "enpkg"


def prompt_engennering(var_dict):

    with open("schema.ttl", "r") as file:
        content = file.read()

    prompt = f"Write me a RDF graph of mass spectrometry spectra and associated features. Here is an exemple schema {content}. \
        You should take the same structure. Here are the data to add in the RDF graph {var_dict}. I want a turtle file and only the file in your response."

    return prompt

spectra_list = load_and_filter_from_mgf("*.mgf")
reference_documents = [SpectrumDocument(s, n_decimals=2) for s in spectra_list]
list_peaks_losses = [doc.words for doc in reference_documents]
ionization_mode = "pos"
mode = True
i = 0
for spectrum, document in zip(spectra_list, list_peaks_losses):

    sample_id = random() * 10000
    usi = f"mzspec:{sample_id}_features_ms2_{ionization_mode}.mgf:scan:{int(spectrum.metadata['feature_id'])}"
    feature_id = term.URIRef(f"lcms_feature_{usi}")
    document_id = term.URIRef(f"spec2vec_doc_{usi}")

    var_dict = {
        name: value
        for name, value in locals().items()
        if name in ["feature_id", "document_id"]
    }
    
    if mode:
        classic()
    else:
        prompt = prompt_engennering(var_dict)
        res = get_chatgpt_response(prompt)
        with open(f"spectrum_{spectrum.metadata['feature_id']}.ttl", "w") as file:
            file.write(res)

        print(res)
        print()

    

    if i >= 3:
        break

    i += 1