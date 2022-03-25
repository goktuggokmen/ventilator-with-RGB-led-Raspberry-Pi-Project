#Final Uygulama Ödevi-4_Proje
#Göktuğ Gökmen & Orkun Şaylığ

from machine import ADC, Pin,  PWM
from time import sleep

sensor_pin = ADC(26)
ldr = machine.ADC(27)
motor = Pin(16,Pin.OUT)
red_led = Pin(17, Pin.OUT)
green_led = Pin(18, Pin.OUT)
red = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(2, Pin.OUT)
buzzer = PWM(Pin(15))

def buzzer_durum(buzzer, on):
    if on:
        buzzer.freq(500)
        buzzer.duty_u16(100000)
    else:
        buzzer.duty_u16(0)
        
def sicaklik_olc(pin_no):
    katsayi = 3.3/ (65535)
    ham_deger = pin_no.read_u16()
    donustur_sicaklik = ham_deger * katsayi
    celcius = donustur_sicaklik/(10.0 / 1000)
    sleep(0.5)
    return celcius

def disco_on(r, g, b):
    #Kırmızı
    r.on()
    g.off()
    b.off()
    sleep(0.2)
    
    #yeşil
    r.off()
    g.on()
    b.off()
    sleep(0.2)
    
    #mavi
    r.off()
    g.off()
    b.on()
    sleep(0.2)
    
    #mor
    r.on()
    g.off()
    b.on()
    sleep(0.2)
    
    #beyaz
    r.on()
    g.on()
    b.on()
    
    
def disco_off(r,g,b):
    r.off()
    g.off()
    b.off()

while True:
    sicaklik = sicaklik_olc(sensor_pin)
    isik_miktari = ldr.read_u16()
    sleep(0.2)
    print("Sicaklik: ",sicaklik, "°C")
    print("Ortam Isigi: ", isik_miktari)
    
    if isik_miktari > 400:
        disco_on(red, green, blue)
    else:
        disco_off(red, green, blue)
      
    if sicaklik > 23:
        motor.on()
        green_led.on()
        red_led.off()
        buzzer_durum(buzzer, True)
        sleep(5)
        buzzer_durum(buzzer, False)
    else:
        motor.off()
        green_led.off()
        red_led.on()