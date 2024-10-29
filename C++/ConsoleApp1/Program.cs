using System; // Directiva necesaria para usar Console

class Program
{
    static void Main(string[] args)
    {
        Automovil fordKa = new Automovil("Ford Ka", 170);
        fordKa.Acelerar(120);
        Console.WriteLine($"Velocidad actual: {fordKa.GetVelocidad()} km/h");
    }
}

class Automovil
{
    private int velocidadMaxima;
    private string marca;
    private int velocidad;

    public Automovil(string marca, int velocidadMax)
    {
        this.marca = marca;
        this.velocidadMaxima = velocidadMax;
        this.velocidad = 0;
    }

    public void Acelerar(int kms)
    {
        int nuevaVelocidad = this.velocidad + kms;
        if (nuevaVelocidad <= this.velocidadMaxima)
        {
            this.velocidad = nuevaVelocidad;
            Console.WriteLine($"El automóvil ha acelerado a {this.velocidad} km/h.");
        }
        else
        {
            this.velocidad = this.velocidadMaxima;
            Console.WriteLine($"El automóvil ha alcanzado su velocidad máxima de {this.velocidadMaxima} km/h.");
        }
    }

    public int GetVelocidad()
    {
        return this.velocidad;
    }
}
