function getTriangleType(jsonString) {
    try {
      // Parse JSON string into JavaScript object
      const { a, b, c } = JSON.parse(jsonString);
  
      // Check if sides can form a triangle
      if (a + b <= c || a + c <= b || b + c <= a) {
        return JSON.stringify({ error: "Invalid input: Sides do not form a triangle" });
      }
  
      // Determine type of triangle
      if (a === b && b === c) {
        return JSON.stringify({ type: "equilateral" });
      } else if (a === b || a === c || b === c) {
        return JSON.stringify({ type: "isosceles" });
      } else {
        return JSON.stringify({ type: "scalene" });
      }
    } catch (error) {
      return JSON.stringify({ error: "Invalid input: " + error.message });
    }
  }
  
