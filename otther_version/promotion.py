from cast_promotion import CastPromotion


class Promotion(CastPromotion):
    def __init__(self, percentage=0, fixed=0):
        self._percentage = percentage
        self._fixed = fixed

    def cast(self, cost):
        cost = max(cost-self._fixed, 0)
        cost = cost * (1-self._percentage)
        return round(cost, 2)
        """ one liner 
        return round(max((cost-self._fixed), 0)*(1-self._percentage), 2)
        """
