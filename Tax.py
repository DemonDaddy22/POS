class Tax:
    __sgst = 2.45
    __cgst = 2.45
    __gst = (__sgst+__cgst)/100
    tax = __gst
    
    @staticmethod
    def getTax():
        return Tax.tax


