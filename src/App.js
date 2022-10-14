import { useState } from "react";
import Cart from "./Cart";
import Product from "./Product";
import "./styles.css";

// Parent containe with state and functionality to add and remove item
export default function App() {
  const products = [
    {
      id: 1,
      name: "Xbox",
      desc: "It is a playstation",
      price: 300,
      quantity: 1
    },
    {
      id: 2,
      name: "Xbox3",
      desc: "It is a playstation",
      price: 100,
      quantity: 1
    },
    {
      id: 3,
      name: "Vgame",
      desc: "It is a playstation",
      price: 100,
      quantity: 1
    },
    {
      id: 4,
      name: "Xbox1",
      desc: "It is a playstation",
      price: 200,
      quantity: 1
    },
    {
      id: 5,
      name: "Xbox2",
      desc: "It is a playstation",
      price: 300,
      quantity: 1
    }
  ];
  const [cart, setCart] = useState([]);

  const addProduct = (item) => {
    var cartItem = [...cart];
    cartItem.push(item);
    setCart(cartItem);
  };

  const removeProduct = (id, e) => {
    var cartItem = [...cart];
    var index = cartItem.findIndex((x) => x.id === id);
    cartItem.splice(index, 1);
    setCart(cartItem);
    e.preventDefault();
  };

  const getProducts = () => {
    var itemList = products.map((item, i) => {
      return (
        <Product item={item} key={i} onAdd={addProduct.bind(this, item)} />
      );
    });
    return itemList;
  };
  return (
    <div>
      {getProducts()}
      <Cart cart={cart} removeItem={removeProduct} />
    </div>
  );
}
