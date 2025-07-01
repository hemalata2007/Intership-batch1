// Identity Card Data
    const person = {
      name: "Hemalata Chaure",
      age: 20,
      course: "Web Development",
      idNumber: "ID-2025-001",
      photo: "sanu.webp"  // Must be in the same folder as this file
    };

    // Fill data into the card
    window.onload = () => {
      document.getElementById("name").textContent = person.name;
      document.getElementById("age").textContent = person.age;
      document.getElementById("course").textContent = person.course;
      document.getElementById("idNumber").textContent = person.idNumber;
      document.getElementById("photo").src = person.photo;
    };
