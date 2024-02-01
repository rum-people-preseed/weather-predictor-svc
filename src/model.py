import prophet


class BasePredictor():
    '''
        This is the abstract class for the BasePredictor. All further predictor are meant to iherit it.
    '''
    def predict(self, next_day: str) -> float:
        '''
            This function predicts the temperature fot the next day based on their coordinates.
        '''
        raise NotImplementedError('This method must be overrided in the derived class!')
    

class ProphetPredictor(BasePredictor):
    '''
        This class provides an implementation for the predictor based on Meta's Prophet API.

        The main idea behind this is to train a bunch of models corresponding to the new location mentioned by the user.
    Therefore we can train the model 'on-demand' by using some kind of script.
    '''
    def __init__(self, place: str):
        self.model = prophet.Prophet()

    
    def predict(self, next_day: str) -> float:
        pass