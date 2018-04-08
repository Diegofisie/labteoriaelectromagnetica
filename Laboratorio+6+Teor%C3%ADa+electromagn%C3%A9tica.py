
# coding: utf-8

# In[261]:

get_ipython().magic('pylab inline')
import numpy as np
import matplotlib.pyplot as plt


# ### Para el agua ###

# In[262]:

datosagua = np.loadtxt("AGUA1.prn") 
datosagua2 = np.loadtxt("AGUA2.prn") 
datosagua3 = np.loadtxt("AGUA3.prn") 


# In[263]:

frecuencia = datosagua[:,0]
eprima = datosagua[:,1]
e2prima = datosagua[:,2]


# In[264]:

frecuencia2 = datosagua2[:,0]
eprima2 = datosagua2[:,1]
e2prima2 = datosagua2[:,2]


# In[265]:

frecuencia3 = datosagua3[:,0]
eprima3 = datosagua3[:,1]
e2prima3 = datosagua3[:,2]


# In[266]:

plt.title('Gráficas primera medición de Agua')
plt.plot(frecuencia,eprima,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecuencia2,eprima2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecuencia3,eprima3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'")
plt.grid(True)


# In[267]:


plt.title('Gráficas primera medición de Agua')
plt.plot(frecuencia,e2prima,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecuencia2,e2prima2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecuencia3,e2prima3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e''")
plt.grid(True)


# In[268]:

frecuenciatotal = frecuencia + frecuencia2 + frecuencia3
frecprom = frecuenciatotal/3
e1tot = eprima + eprima2 + eprima3 
e1prom = e1tot/3
plt.title('Gráfica promedio para el agua e´')
plt.plot(frecprom,e1prom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e' promedio")
plt.grid(True)


# In[269]:


e2tot = e2prima + e2prima2 + e2prima3 
e2prom = e2tot/3
plt.title('Gráfica promedio para el agua e´´')
plt.plot(frecprom,e2prom,linewidth = 1.0,  label = 'e2')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'' promedio")
plt.grid(True)


# ### Para el etanol"###

# In[270]:

datosetanol = np.loadtxt("ETANOL1.prn") 
datosetanol2 = np.loadtxt("ETANOL2.prn") 
datosetanol3 = np.loadtxt("ETANOL3.prn") 


# In[271]:

freceta = datosetanol[:,0]
eprimaeta = datosetanol[:,1]
e2primaeta = datosetanol[:,2]

freceta2 = datosetanol2[:,0]
eprimaeta2 = datosetanol2[:,1]
e2primaeta2 = datosetanol2[:,2]

freceta3 = datosetanol[:,0]
eprimaeta3 = datosetanol3[:,1]
e2primaeta3 = datosetanol3[:,2]


# In[272]:

plt.title('Gráficas primera medición del Etanol')
plt.plot(freceta,eprimaeta,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(freceta2,eprimaeta2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(freceta3,eprimaeta3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'")
plt.grid(True)


# In[273]:

plt.title('Gráficas primera medición del Etanol')
plt.plot(freceta,e2primaeta,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(freceta2,e2primaeta2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(freceta3,e2primaeta3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e''")
plt.grid(True)


# In[274]:

frecetciatotal = freceta + freceta2 + freceta3
frecetprom = frecetciatotal/3
e1ettot = eprimaeta + eprimaeta2 + eprimaeta3 
e1etprom = e1ettot/3
plt.title('Gráfica promedio para el etanol e´')
plt.plot(frecetprom,e1etprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e' promedio")
plt.grid(True)


# In[275]:

e2ettot = e2primaeta + e2primaeta2 + e2primaeta3 
e2etprom = e2ettot/3
plt.title('Gráfica promedio para el etanol e´´')
plt.plot(frecetprom,e2etprom,linewidth = 1.0,  label = 'e2')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'' promedio")
plt.grid(True)


# ### Para el Metanol###

# In[276]:

datosmet = np.loadtxt("METANOL1.prn") 
datosmet2 = np.loadtxt("METANOL2.prn") 
datosmet3 = np.loadtxt("METANOL3.prn") 

frecmet= datosmet[:,0]
eprimet = datosmet[:,1]
e2primet = datosmet[:,2]

frecmet2= datosmet2[:,0]
eprimet2 = datosmet2[:,1]
e2primet2 = datosmet2[:,2]

frecmet3= datosmet3[:,0]
eprimet3 = datosmet3[:,1]
e2primet3 = datosmet3[:,2]


# In[277]:

plt.title('Gráficas primera medición del Metanol')
plt.plot(frecmet,eprimet,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecmet2,eprimet2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecmet3,eprimet3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'")
plt.grid(True)


# In[278]:

plt.title('Gráficas primera medición del Metanol')
plt.plot(frecmet,e2primet,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecmet2,e2primet2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecmet3,e2primet3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e''")
plt.grid(True)


# In[279]:

frecmetot = frecmet + frecmet2 + frecmet3
frecmetprom = frecmetot/3
e1mettot = eprimet + eprimet2 + eprimet3 
e1metprom = e1mettot/3
plt.title('Gráfica promedio para el metanol e´')
plt.plot(frecmetprom,e1metprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e' promedio")
plt.grid(True)


# In[280]:

e2mettot = e2primet + e2primet2 + e2primet3 
e2metprom = e2mettot/3
plt.title('Gráfica promedio para el metanol e´´')
plt.plot(frecmetprom,e2metprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e''  promedio")
plt.grid(True)


# ### Para la leche entera###

# In[281]:

datosleche = np.loadtxt("LECHEENTERA1.prn") 
datosleche2 = np.loadtxt("LECHEENTERA2.prn") 
datosleche3 = np.loadtxt("LECHEENTERA3.prn") 


# In[282]:

frecleche= datosleche[:,0]
eprimaleche = datosleche[:,1]
e2primaleche = datosleche[:,2]
frecleche2= datosleche2[:,0]
eprimaleche2 = datosleche2[:,1]
e2primaleche2 = datosleche2[:,2]
frecleche3= datosleche3[:,0]
eprimaleche3 = datosleche3[:,1]
e2primaleche3 = datosleche3[:,2]


# In[283]:

plt.title('Gráficas primera medición Leche entera')
plt.plot(frecleche,eprimaleche,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecleche2,eprimaleche2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecleche3,eprimaleche3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'")
plt.grid(True)


# In[284]:

plt.title('Gráficas primera medición Leche entera')
plt.plot(frecleche,e2primaleche,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(frecleche2,e2primaleche2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(frecleche3,e2primaleche3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e''")
plt.grid(True)


# In[285]:

freclechetot = frecleche+frecleche2+frecleche3
freclecheprom = freclechetot/3
eprimalechetot = eprimaleche+eprimaleche2+eprimaleche3
eprimalecheprom = eprimalechetot/3
plt.title('Gráfica promedio para la leche entera e´')
plt.plot(freclecheprom,eprimalecheprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e'  promedio")
plt.grid(True)


# In[286]:

e2primalechetot = e2primaleche+e2primaleche2+e2primaleche3
e2primalecheprom = e2primalechetot/3
plt.title('Gráfica promedio para la leche entera e´´' )
plt.plot(freclecheprom,e2primalecheprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e''  promedio")
plt.grid(True)


# ### Para la leche descremada

# In[287]:

datoslechedes = np.loadtxt("lECHEDESLACTDOSADA1.prn") 
datoslechedes2 = np.loadtxt("LECHEDESLACTOSADA2.prn") 
datoslechedes3 = np.loadtxt("LECHEDESLACTOSADA3.prn") 
freclechedes= datoslechedes[:,0]
eprimalechedes = datoslechedes[:,1]
e2primalechedes = datoslechedes[:,2]
freclechedes2= datoslechedes2[:,0]
eprimalechedes2 = datoslechedes2[:,1]
e2primalechedes2 = datoslechedes2[:,2]
freclechedes3= datoslechedes3[:,0]
eprimalechedes3 = datoslechedes3[:,1]
e2primalechedes3 = datoslechedes3[:,2]


# In[288]:

plt.title('Gráficas primera medición Leche Deslactosada')
plt.plot(freclechedes,eprimalechedes,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(freclechedes2,eprimalechedes2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(freclechedes3,eprimalechedes3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e'")
plt.grid(True)


# In[289]:

plt.title('Gráficas primera medición Leche Deslactosada')
plt.plot(freclechedes,e2primalechedes,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.plot(freclechedes2,e2primalechedes2,linewidth = 1.0, label = 'e2')
plt.legend(loc= 0)
plt.plot(freclechedes3,e2primalechedes3,linewidth = 1.0, label = 'e3')
plt.legend(loc= 0)
plt.ylabel("Frecuncia[Hz]")
plt.xlabel("e''")
plt.grid(True)


# In[290]:

freclechedestot = freclechedes+freclechedes2+freclechedes3
freclechedesprom = freclechedestot/3
eprimalechedestot = eprimalechedes+eprimalechedes2+eprimalechedes3
eprimalechedesprom = eprimalechedestot/3
plt.title('Gráfica promedio para la leche deslactosada e´')
plt.plot(freclechedesprom,eprimalechedesprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e'  promedio")
plt.grid(True)


# In[291]:

e2primalechedestot = e2primalechedes+e2primalechedes2+e2primalechedes3
e2primalechedesprom = e2primalechedestot/3
plt.title('Gráfica promedio para la leche deslactosada e´´')
plt.plot(freclechedesprom,e2primalechedesprom,linewidth = 1.0,  label = 'e1')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e'' promedio")
plt.grid(True)


# ### Todos los promedios de e'###

# In[292]:

plt.title('Gráfica de todos los promedios de e´')
plt.plot(frecprom,e1prom,linewidth = 1.0,  label = 'Agua')
plt.legend(loc= 0)
plt.plot(frecetprom,e1etprom,linewidth = 1.0,  label = 'Etanol')
plt.legend(loc= 0)
plt.plot(frecmetprom,e1metprom,linewidth = 1.0,  label = 'Metanol')
plt.legend(loc= 0)
plt.plot(freclecheprom,eprimalecheprom,linewidth = 1.0,  label = 'Leche entera')
plt.legend(loc= 0)
plt.plot(freclechedesprom,eprimalechedesprom,linewidth = 1.0,  label = 'Leche des')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e' promedio")
plt.grid(True)


# In[293]:

plt.title('Gráfica de todos los promedios de e´´' )
plt.plot(frecprom,e2prom,linewidth = 1.0,  label = 'agua')
plt.legend(loc= 0)
plt.plot(frecetprom,e2etprom,linewidth = 1.0,  label = 'etanol')
plt.legend(loc= 0)
plt.plot(frecmetprom,e2metprom,linewidth = 1.0,  label = 'metanol')
plt.legend(loc= 0)
plt.plot(freclecheprom,e2primalecheprom,linewidth = 1.0,  label = 'Leche entera')
plt.legend(loc= 0)
plt.plot(freclechedesprom,e2primalechedesprom,linewidth = 1.0,  label = 'Leche des')
plt.legend(loc= 0)
plt.ylabel("Frecuencia[Hz]")
plt.xlabel("e''  promedio")
plt.grid(True)


# In[ ]:



