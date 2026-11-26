from data_provider.data_loader import Dataset_Crossformer_Fusion
from utils.CustomTokenizer import CustomTokenizer

test = Dataset_Crossformer_Fusion("./dataset", features='M', timeenc=1)
test.__read_data__()
#this is a testing file I used for verifying the custom reading and tokenizing was working