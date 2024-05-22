from sentence_transformers import SentenceTransformer, util
import pandas as pd

from evaluation._services.factories.evaluation_strategies.level_strategy import LevelStrategy
from evaluation._services.visualiser import display_pie_chart


class ExplanationLevelStrategy(LevelStrategy):

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def _cosine_similarity(self, text1, text2):

        embeddings1 = self.model.encode(text1, convert_to_tensor=True)
        embeddings2 = self.model.encode(text2, convert_to_tensor=True)

        cosine_similarity_result = util.pytorch_cos_sim(embeddings1, embeddings2)

        return cosine_similarity_result.item()

    def _get_result(self, valid_df, context_df):

        results = [self._cosine_similarity(text1, text2) for text1, text2 in
                   zip(valid_df['relevance explanation'],
                       context_df['relevance explanation'])]

        df_results = pd.DataFrame({'Cosine Similarity': results})
        return df_results

    def evaluate(self, validation_context, contexts):

        print("Rationale evaluation")

        for context in contexts:
            valid_match_indexes = validation_context.dataframe['label'] == context.dataframe['label']

            valid_df = validation_context.dataframe[valid_match_indexes]
            context_df = context.dataframe[valid_match_indexes]

            result = self._get_result(valid_df, context_df)

            display_pie_chart(result['Cosine Similarity'])








