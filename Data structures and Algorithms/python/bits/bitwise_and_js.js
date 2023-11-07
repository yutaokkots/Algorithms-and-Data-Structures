let lst1 = ["hello", "battery", "headphone", "toilet paper", "sticker"]
let lst2 = ["hat","toilet paper","captain","wrench","battery"]
//let lst3 = ["boat", "toilet paper", "ninja", "smoke"]

let set1 = new Set(lst1)
let set2 = new Set(lst2)

console.log(set1)
// Set(5) { 'hello', 'battery', 'headphone', 'toilet paper', 'sticker' }

let intersection = new Set([...set1].filter(item => set2.has(item)));

console.log(intersection)
// Set(2) { 'battery', 'toilet paper' }