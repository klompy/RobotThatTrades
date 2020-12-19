import os
print(os.listdir())

class Portfolio():
    def __init__(self, cash=0):
        self.positions = {}
        self.cash = cash        #Naively in add_position, need system to ensure we do not spend cash we do not have, signal trade completion
        self.market_value = 0   #Not implemented
        self.profit_loss = 0    #Not Implemented
        self.risk_tolerance = 0 #Not implemented
    
    # Add a position
    # Buying -> Quantity is positive, Selling -> Quantity is negative
    # Purchase price should always be positive, even when shorting
    def add_position(self, symbol: str, purchase_date: str, asset_type: str, quantity: int = 0, purchase_price: float = 0.0) -> dict:        
        # If new symbol - no previous positions on it
        if self.isEmpty(symbol) is False: 
            # Setup dictionary for symbol
            self.positions[symbol] = {}
            self.positions[symbol]['symbol'] = symbol
            # Set quantity 0 so we can += our quantity in the future
            self.positions[symbol]['quantity'] = 0
            # Fix the asset type permanently
            self.positions[symbol]['asset_type'] = asset_type #Perhaps make this argument optional since it only gets used for the first position on the symbol
            self.positions[symbol]['ID'] = []
            # Create lists for purchase price/date so we can graph and track our trades over the course of a backtest
            self.positions[symbol]['purchase_price'] = []
            self.positions[symbol]['purchase_date'] = []
            
        # No else as we did not add the quantity/purchase info if there was a setup
        #self.positions[symbol]['ID'].append(Order())
        self.positions[symbol]['quantity'] += quantity 
        self.positions[symbol]['purchase_price'].append(purchase_price)
        self.positions[symbol]['purchase_date'].append(purchase_date)
        self.cash = self.cash - (quantity*purchase_price) # This is naive and does not check if we have sufficient funds
        
        return self.positions[symbol] #Return dictionary on symbol
    
    # Checks if there is a dictionary created for a given symbol. This implies there has been a position on the symbol since portfolio creation
    def isEmpty(self, symbol: str):
        # If no Key Error, return True
        try:
            self.positions[symbol]
            return True
        except:
            return False
