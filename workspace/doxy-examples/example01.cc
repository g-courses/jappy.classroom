#include <iostream>
#include <string>
#include <cstdlib>


class Animal {
    protected:
    std::string sonido;

    public:
    /**
     * @brief Construct a new Animal object
     * 
     */
    Animal(){
        sonido = "no definido";
    }

    /**
     * @brief 
     * 
     */
    void vocalizar() {
        std::cout << sonido << "\n";
    }
};


class Mascota: public Animal {
    private:
    std::string nombreMascota;

    public:
    /**
     * @brief Construct a new Mascota object
     * 
     */
    Mascota(){

    }

    /**
     * @brief asigna el nombre de la mascota
     * 
     * @param nombre string que representa el nombre
     */
    void nombre(std::string nombre){
        nombreMascota = nombre;
    }

    std::string nombre(){
        return(nombreMascota);
    }

};

class Perro: public Mascota {
    public:
    Perro(){
        sonido = "ladrar";
    }
};

class Gato: public Mascota {
    public:
    Gato(){
        sonido = "maullar";
    }
};

class Lobo: public Animal {
    public:
    Lobo(){
        sonido = "aullar";
    }
};


void sonidoAnimal(Animal a){
    a.vocalizar();
}


int main(int argc, char* argv[]){

    Mascota miPerro = Perro();
    Gato gatoBar =  Gato();
    Animal loboBosque = Lobo();

    miPerro.vocalizar();
    gatoBar.vocalizar();
    loboBosque.vocalizar();

    sonidoAnimal(miPerro);
    sonidoAnimal(gatoBar);
    sonidoAnimal(loboBosque);

    miPerro.nombre("Inti");
    gatoBar.nombre("Kitty");

    std::cout << "miPerro.nombre() = " << miPerro.nombre() << "\n";

    return(EXIT_SUCCESS);
}