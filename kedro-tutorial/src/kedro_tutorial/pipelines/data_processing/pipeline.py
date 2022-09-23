"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                # pasar la funación que necesito
                func=preprocess_companies,
                # la tabla de entrada
                inputs="companies",
                # nombre de la salida en el entorno
                outputs="preprocessed_companies",
                # nombre que le voy a dar al nodo
                name="preprocess_companies_node_ejemplo",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            # node(
            #     func=create_model_input_table,
            #     inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
            #     outputs="model_input_table",
            #     name="create_model_input_table_node",
            # ),
        ]
    )
