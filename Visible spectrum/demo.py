# -*- coding: utf-8 -*-
import spectrum
def main():

    print("--------------------")
    print("| codedrome.com        |")
    print("| Visible Spectrum     |")
    print("| updated by jshederer |")
    print("--------------------\n")

    data = spectrum.generate_data()

    spectrum.print_data(data)

    spectrum.plot_wavelength_frequency(data, "wavelength_frequency.png")

    spectrum.plot_frequency_wavelength(data, "frequency_wavelength.png")

main()