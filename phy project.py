import math
import numpy as np

def nr():
    while True:
        print("\n")
        print("1. Radius of Mth dark ring")
        print("2. Radius of Mth bright ring")
        print("3. Wavelength of the light used")
        print("4. Back to main menu")
        ch=int(input("Enter your choice:  "))
        print("\n")
        if ch==1:
            m=int(input("Enter the value of M: "))
            R=eval(input("Enter the radius of curvature of plano-convex lens in cm: "))
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            r = (math.sqrt(m*R*l/10))/1000
            print("radius of ",m,"th dark ring is ",r," cm.")
        elif ch==2:
            m=int(input("Enter the value of M: "))
            R=eval(input("Enter the radius of curvature of plano-convex lens in cm: "))
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            r = (math.sqrt((m+0.5)*R*l/10))/1000
            print("radius of ",m,"th bright ring is ",r," cm.")
        elif ch==3:
            print("Wavelength = (Dm+p)^2 - (Dm)^2 / 4pR")
            p=int(input("Enter the value of p in the above formula: "))
            R=eval(input("Enter the radius of curvature of plano-convex lens in cm: "))
            D2=eval(input("Enter the diameter of(m+p)th ring in cm: "))
            D1=eval(input("Enter the diameter of mth ring in cm: "))
            w=((D2**2)-(D1**2))*(10**7)/(4*p*R)
            print("Wavelength of the light used is ",w,"nano-metres.")
        elif ch==4:
            break
        else:
            print("Wrong choice....Enter again.")

def cl():
    while True:
        print("\n")
        print("Cosine law is used to find the optical path difference.")
        N=eval(input("Enter the refractive index of the medium in which light entered: "))
        d=eval(input("Enter the thickness of the medium in cm: "))
        t=eval(input("Enter the angle of refraction of the light in degrees: "))
        cos=math.cos(np.pi*t/180)
        pd=2*N*d*cos
        print("The optical path difference is ",pd,"cm.")
        break

def interbyw():
    while True:
        print("\n")
        print("1. Resultant Intensity") 
        print("2. Maximum and minimum resultant intensity")
        print("3. Resultant Amplitude")
        print("4. Maximum and minimum resultant amplitude")
        print("5. Fringe width of interference pattern in YDSE")
        print("6. Shifting of fringe pattern when a sheet is introduced in front of one of the slits in YDSE")
        print("7. Back to Main Menu")
        ch=int(input("Enter your choice:  "))
        if ch==5:
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            D=eval(input("Enter distance between slits and screen in cm: "))
            d=eval(input("Enter the distance between the slits in mm: "))
            b=(l*D)/(d*100000)
            print("The fringe width of the pattern is",b,"mm.")
        elif ch==1:
            i1=eval(input("Enter the intensity by first source in W/m^2: "))
            i2=eval(input("Enter the intensity by second source in W/m^2: "))
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            x=eval(input("Enter the path difference in nano-metres: "))
            ph=(44*x)/(l*7)
            i=i1+i2+(2*math.sqrt(i1*i2)* math.cos(np.pi*ph/180))
            print("The resultant intensity is",i,"W/m^2")
        elif ch==2:
            i1=eval(input("Enter the intensity produced by first source in W/m^2: "))
            i2=eval(input("Enter the intensity produced by second source in W/m^2: "))
            max=(math.sqrt(i1)+math.sqrt(i2))**2       
            min=(math.sqrt(i1)-math.sqrt(i2))**2
            print("The maximum reslutant intensity is",max,"W/m^2 and the minimum resultant intensity is",min,"W/m^2")
        elif ch==3:
            a=eval(input("Enter the amplitude of first wave in metres: "))
            b=eval(input("Enter the amplitude of second wave in metres: "))
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            x=eval(input("Enter the path difference in nano-metres: "))
            ph=(44*x)/(l*7)
            R=math.sqrt(a**2+b**2+2*a*b*math.cos(np.pi*ph/180))
            print("The resultant amplitude is",R,"metres.")
        elif ch==4:
            a=eval(input("Enter the amplitude of first wave in metres: "))
            b=eval(input("Enter the amplitude of second wave in metres: "))
            max=a+b
            min=abs(a-b)
            print("The maximum reslutant amplitude is",max,"metres and the minimum resultant amplitude is",min,"metres.")
        elif ch==6:
            D=eval(input("Enter distance between slits and screen in cm: "))
            d=eval(input("Enter the distance between the slits in mm: "))
            n=eval(input("Enter the refractive index of the sheet: "))
            t=eval(input("Enter the thickness of the sheet in mm: "))
            sh=D*(n-1)*t*10/d
            print("The fringe pattern gets shifted by a distance",sh,"mm.")
        elif ch==7:
            break
        else:
            print("Wrong choice....enter again.")

def dg():
    while True:
        print("\n")
        print("1. Calculate number of lines per unit length")
        print("2. Calculate wavelength of light")
        print("3. Back to Main Menu")
        ch=int(input("Enter your choice:  "))
        if ch==1:
            th=eval(input("Enter the diffraction angle in degrees: "))
            n=eval(input("Enter the order of the spectrum: "))
            l=eval(input("Enter the wavelength of light in nano-metres: "))
            N=math.sin(np.pi*th/180)/(n*l)*10**9
            print("The number of lines per unit length of the grating is",N)
        elif ch==2:
            th=eval(input("Enter the diffraction angle in degrees: "))
            n=eval(input("Enter the order of the spectrum: "))
            N=eval(input("Enter number of lines per unit length of the grating: "))
            l=math.sin(np.pi*th/180)/(n*N)*10**9
            print("The wavelength of the light is",l,"nm.")
        elif ch==3:
            break;
        else:
            print("Wrong choice....enter again.")

def rp():
    while True:
        print("\n")
        print("1. Resolving power of a grating")
        print("2. Resolving power of a telescope")
        print("3. Resolving power of a prism")
        print("4. Back to Main menu")
        ch=int(input("Enter your choice:  "))
        if ch==1:
            n=eval(input("Enter the order of the spectrum: "))
            N=eval(input("Enter the total number of slits in the grating: "))
            rp=n*N
            print("The resolving power of grating for order",n,"is",rp)
        elif ch==2:
            D=eval(input("Enter the diameter of the objective lens aperture in cm: "))
            l=eval(input("Enter the wavelength of the light used in nano-metres: "))
            rp=(D*(10**7))/(1.22*l)
            print("The resolving power of the telescope is",rp)
        elif ch==3:
            t=eval(input("Enter the width of the base of prism in cm: "))
            B=eval(input("Enter the Cauchy's constant B in cm^2: "))
            l=eval(input("Enter the wavelength of the light used in nano-metres: "))
            rp=2*B*t*(10**21)/(l**3)
            print("The resolving power of the prism is",rp)
        elif ch==4:
            break
        else:
            print("Wrong choice....enter again.")

def of():
    while True:
        print("\n")
        n=eval(input("Enter the refractive index of the medium outside the fibre: "))
        n1=eval(input("Enter the refractive index of core: "))
        n2=eval(input("Enter the refractive index of cladding: "))
        if n2>n1:
            print("RI of cladding cannot be greater than that of core")
            break
        na=(math.sqrt(n1**2 - n2**2))/n
        if na>=1:
            print("Invalid values entered.")
            break
        aa=(math.asin(na))*1260/22
        print("The numerical aperture is",na,"and the acceptance angle is",aa,"degrees.")
        break
    
            
def main():
    while True:
        print("\n")
        print("\t\t\tMade by Siddharth Kalkal and Kamal Kumar")
        print("*********************************************************************************")
        print("\t\t\tProgram to solve various formulas of Optics")
        print("*********************************************************************************")
        print("Choose the topic related to the required formula")
        print("1. Newton's Rings")
        print("2. Cosine Law")
        print("3. Interference by division of wavefront")
        print("4. Diffraction Grating")
        print("5. Resolving Power")
        print("6. Numerical Aperture and Acceptance Angle of Optical fibre")
        print("7. Exit") 
        ch=int(input("Enter your choice:  "))
        if ch==1:
            nr()
        elif ch==2:
            cl()
        elif ch==3:
            interbyw()
        elif ch==4:
            dg()
        elif ch==5:
            rp()
        elif ch==6:
            of()
        elif ch==7:
            print("Thank You.....Come again soon")
            break
        else:
            print("Wrong Choice.....Enter Again")

main()

