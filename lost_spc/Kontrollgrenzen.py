def sigma_range_mu(data):
    mu = data.mean(axis=1)
    mu_mean = mu.mean()
    range = data.max(axis=1) - data.min(axis=1)
    range_mean = range.mean()
    sigma = data.std(axis=1, ddof=1)
    sigma_mean = sigma.mean()
    return mu_mean, range_mean, sigma_mean

def shewhart_constants_r(m, sim_size=10000000):
    X = st.norm.rvs(size=(sim_size, m)) 
    R_i = X.max(axis=1) - X.min(axis=1)
    d2 = np.mean(R_i)
    d3 = np.std(R_i, ddof=1)
    return d2, d3

def Kontrollgrenzen_R_Karte(data,m):
    # Aufruf der sigma_range_mu Funktion und Extrahieren der Werte
    d2, d3 = shewhart_constants_r(m)
    _, R_mean, _ = sigma_range_mu(data)
    UCL = R_mean + 3 * d3 / d2 * R_mean
    CL = R_mean
    LCL = R_mean - 3 * d3 / d2 * R_mean
    if LCL < 0:
        LCL = 0
    return UCL, CL, LCL

def Kontrollgrenzen_x_Karte(data,m):
    d2, d3 = shewhart_constants_r(m)  
    x_mean,R_mean, _ = sigma_range_mu(data)
    UCL_x = x_mean + 3 * R_mean / d2 / math.sqrt(m)
    C_x = x_mean
    LCL_x = x_mean - 3 * R_mean / d2 / math.sqrt(m)
    return UCL_x, C_x, LCL_x

def shewhart_constants_s(m):
    return gamma(m/2)/gamma((m-1)/2)*np.sqrt(2/(m-1))

def Kontrollgrenzen_s_Karte(data,m):
    c4 = shewhart_constants_s(m) 
    _,_, s_i_mean = sigma_range_mu(data)
    UCL_s = s_i_mean + 3 * math.sqrt(1 - c4**2) / c4 * s_i_mean
    CL_s = s_i_mean
    LCL_s = s_i_mean - 3 * math.sqrt(1 - c4**2) / c4 * s_i_mean
    return UCL_s, CL_s, LCL_s