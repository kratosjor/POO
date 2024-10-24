// Solicita la edad al usuario
let edad = prompt("Por favor, ingresa tu edad:");

// Convierte el valor ingresado a un número
edad = parseInt(edad);

// Verifica en qué rango de edad se encuentra el usuario
if (edad < 13) {
  alert("Eres un niño.");
} else if (edad >= 13 && edad <= 17) {
  alert("Eres un adolescente.");
} else if (edad >= 18 && edad <= 64) {
  alert("Eres un adulto.");
} else if (edad >= 65) {
  alert("Eres un adulto mayor.");
} else {
  alert("Por favor, ingresa una edad válida.");
}
