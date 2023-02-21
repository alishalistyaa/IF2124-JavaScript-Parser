try {
  let a = 1;
  if (a == 1) {
    throw "Error";
  }
  console.log("Do something");
} catch (e) {
  a = 1;
  console.log(e);
} finally {
  a = 1;
  console.log("Finally");
}
