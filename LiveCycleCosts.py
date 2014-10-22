# -*- coding: utf-8 -*-
class LiveCycleCosts():
    """i = Zinssatz (in Teilen)"""
    def __init__(self, i):
        self.i = i
        self.npv = 0
        self.summe = 0
        self.log = "initialisiert! \n"
        
    def addiere(self,Z,T,t=1):
        """Z = Kapital, T = bis und mit Jahr, [t = ab Jahr]"""
        self.log += "ADDITION: \nSumme;NPV \n%s;%s \n---\n"%(self.summe,self.npv)
        for k in range(t,T+1):
            self.npv += Z/(1+self.i)**k
            self.summe += Z
            self.log += "%s;%s \n"%(Z,Z/(1+self.i)**k)
        self.log += "--- \n%s;%s \n"%(self.summe,self.npv)

    def subtrahiere(self,Z,T,t=1):
        """Z = Kapital, T = bis und mit Jahr, [t = ab Jahr]"""
        self.log += "SUBTRAKTION: \nSumme;NPV \n%s;%s \n---\n"%(self.summe,self.npv)
        for k in range(t,T+1):
            self.npv -= Z/(1+self.i)**k
            self.summe -= Z
            self.log += "-%s;-%s \n"%(Z,Z/(1+self.i)**k)
        self.log += "--- \n%s;%s \n"%(self.summe,self.npv)

    def verteile(self,T):
        """T = anzahl Jahre, auf die verteilt wird"""
        self.annuitaet = ((self.i*(1+self.i)**T)/(((1+self.i)**T)-1))*self.npv
        self.jaehrl = self.summe/T
        self.log += "Mittl. jährl. Kosten;annuität \n%s;%s \n"%(self.jaehrl,self.annuitaet)

    def setze(self,Summe,NPV):
        """Summe = setze die Summe auf den eingegebenen Wert
        NPV = setze den NPV auf den eingegebenen Wert"""
        self.summe = Summe
        self.npv = NPV

    def printlog(self):
        print(self.log)
