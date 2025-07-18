#include <iostream>
#include <string>
#include <cstdlib>


class NombreApellidos{
    private:
    std::string nombre;
    std::string apellido1;
    std::string apellido2;

    public:
    NombreApellidos(){

    }

    NombreApellidos(std::string _nombre, std::string _apellido1, std::string _apellido2){
        nombre = _nombre;
        apellido1 = _apellido1;
        apellido2 = _apellido2;
    }

    NombreApellidos( NombreApellidos& n){
        nombre = n.nombre;
        apellido1 = n.apellido1;
        apellido2 = n.apellido2;
    }

    std::string toString(){
        return(nombre + " " + apellido1 + " " + apellido2);
    }

};

class Direccion{
    private:
    std::string calle;
    int         numero;
    std::string ciudad;

    public:
    Direccion(){}

    Direccion(std::string _calle, int _numero, std::string _ciudad){
        calle  = _calle;
        numero = _numero;
        ciudad = _ciudad;
    }

    Direccion(Direccion& d){
        calle  = d.calle;
        numero = d.numero;
        ciudad = d.ciudad;
    }

    std::string toString(){
        return(calle + " " + std::to_string(numero) + " " + ciudad);
    }
};


class Persona {
    private:
    NombreApellidos nombreCompleto;
    std::string paisOrigen;
    int edad;
    Direccion direccion;

    public:
    Persona(){}

    Persona(NombreApellidos _nombreCompleto, 
             std::string _paisOrigen , 
             int _edad, Direccion _direccion): nombreCompleto(_nombreCompleto),
                                               direccion(_direccion){
        paisOrigen = _paisOrigen;
        edad       = _edad;
    }
    
    Persona(Persona& p):  nombreCompleto(p.nombreCompleto), direccion(p.direccion){
        paisOrigen = p.paisOrigen;
        edad       = p.edad;
    }
    

    // Método para mostrar información
    std::string toString() {
        return( nombreCompleto.toString() + "," + paisOrigen + "," + std::to_string(edad) + "," + direccion.toString() );
    }

};

class Estudiante: public Persona{
    private:
    std::string carrera;

    public:
    Estudiante(NombreApellidos _nombreCompleto, 
             std::string _paisOrigen , 
             int _edad, 
             Direccion _direccion,
             std::string _carrera): Persona(_nombreCompleto, _paisOrigen, _edad, _direccion) {
        
        carrera = _carrera;
    }

    std::string toString(){
        return( Persona::toString() + " , " + carrera );
    }
}; 


void pruebaPersonas(){
    NombreApellidos nn("nombre","apellido","apellido02");
    Direccion       dd("calle", 10, "Valparaiso");
    Estudiante p0 = Estudiante(nn, "Chile",45, dd, "info"); 

     std::cout << p0.toString() << "\n";   

    /*
    Persona* personas = nullptr;

    int size = 100000;
    personas = new Persona[size];

    for(int i = 0; i < size+30; i++){
        std::cout << i << "\n";
        NombreApellidos nn("nombre"+std::to_string(i),"apellido"+std::to_string(i),"apellido02");
        Direccion       dd("calle"+std::to_string(i), i, "Valparaiso"+std::to_string(i));
        personas[i] = Persona(nn, "Chile"+std::to_string(i),i, dd);        
    }

    for(int i = 0; i < size; i++){
        std::cout << i << ":" << personas[i].toString() << "\n";     
    }
    */
}


/*
 *  Clase zona circular
 */

 class Coordenadas {
    private:
    double longitud;
    double latitud;

    public:
    Coordenadas(double _long, double _lat){
        longitud = _long;
        latitud  = _lat;
    }

    Coordenadas(Coordenadas& c){
        longitud = c.longitud;
        latitud  = c.latitud;
    }

    std::string toString(){
        return ("[" + std::to_string(longitud) + " , " + std::to_string(latitud)  + "]");
    }
 };

 class Circulo {
    private:
    Coordenadas coords;
    double radio;

    public:
    Circulo(double _longitud, double _latitud, double _radio): coords(_longitud, _latitud) {
        radio = _radio;
    }

     Circulo(Coordenadas _coords, double _radio): coords(_coords) {
        radio = _radio;
    }

    std::string toString(){
        return( coords.toString() + " ==> " + std::to_string(radio) );
    }
 };

 void pruebasCirculo(){
    Circulo c0 = Circulo(-33.045855, -71.613220, 45);
    std::cout << c0.toString() << "\n";

    Coordenadas coords = Coordenadas(-33.0493094,-71.6086095);
    Circulo c1 = Circulo(coords, 60);

     std::cout << c1.toString() << "\n";


 }

int main(int argc, char* argv[]){
    pruebaPersonas();
    pruebasCirculo();
    return(EXIT_SUCCESS);
}

