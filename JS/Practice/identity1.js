const person1 = {
      name: "Hemalata Chaure",
      age: 20,
      course: "Web Development",
      idNumber: "ID-2025-001",
      photo: "sanu.webp"
    };

    document.getElementById("name1").textContent = person1.name;
    document.getElementById("age1").textContent = person1.age;
    document.getElementById("course1").textContent = person1.course;
    document.getElementById("id1").textContent = person1.idNumber;
    document.getElementById("photo1").src = person1.photo;