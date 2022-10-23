

def main():
        
        ball_user =  input('What is the color of the ball: ')
        amount_pay = int(input('What is the amount of pay: '))
        
        white_ball = 0
        green_ball = 0.20
        purple_ball = 0.35
        blueclaire_ball = 0.60
        red_ball = 0.100
        


        if ball_user == 'white':
            print (f'You will pay {amount_pay} * {white_ball}')
        if ball_user == 'green':
            print ("Bolita verde.")
        if ball_user == 'green':
            print ("Bolita amarilla.")
        if ball_user == 'green':
            print ("Bolita azul.")
        if ball_user == 'green':
            print ("Bolita roja.")
        
        # result = amount_pay - discount
            
        # print ("Valor de bolita: " + bolita)
        # print ("Valor de cantidad a pagar: " + cantidad_a_pagar)
        # print ("Valor de descuento: " + discount)

if __name__ == '__main__':
    main()