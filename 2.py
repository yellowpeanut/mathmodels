

def find_m_out():
    sig = 0



def find_dM(m_in, m_out, Tv):
    kt = 5000
    F = 10
    Ts = 90
    r = 2260000
    ct = 4187
    return (r*m_in - r*m_out - kt*F*(Tv-Ts)-(m_in-m_out)*ct*Ts) \
           / (r - ct*Ts)


def find_dC_out(C_in, C_out, m_in, m_out, M, dM):
    return (m_in*C_in - m_out*C_out - C_out*dM) \
           / M


def