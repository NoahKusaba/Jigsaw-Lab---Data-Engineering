class Bundle:
    def price(self):
        if self.weight < 5:
            return 10
        else:
            return 10 + (self.weight - 5)*1.5
    
    def processingDays(self):
        month_difference = self.ready_month - self.dropoff_month
        day_difference = self.ready_day -  self.dropoff_day
        return month_difference*30 + day_difference
    
    def holdingDays(self):
        month_difference = self.pickup_month - self.dropoff_month
        day_difference = self.ready_day -  self.dropoff_day
        return month_difference*30 + day_difference