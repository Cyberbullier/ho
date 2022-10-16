import axios from "axios";
import Header from './components/Header';
import Main from './components/Main';
import Cart from './components/Cart';
import data from './dataRef';
import { useState } from 'react';


function App() {
  const { products } = data;
  const [cartItems, setCartItems] = useState([]);
  const onAdd = (product) => {

<<<<<<< HEAD
      axios.post('https://joestar-mushroom-farm.herokuapp.com/decrement-stock', {
=======
      axios.post('http://127.0.0.1:5000/decrement-stock', {
>>>>>>> 11628b8 (fixed routing issue)
        name: product.name
      })
      .then((res) => {
        let res_body = res.data
        console.log(`decremented ${product.name} stock by ${res_body.added}`)
        console.log(`Current inventory for ${product.name}: ${res_body.current_stock} `)
        const exist = cartItems.find((x) => x.id === product.id);
        if (res_body.added == 0)return;
        if (exist){
        setCartItems(
          cartItems.map((x) =>
            x.id === product.id ? { ...exist, qty: exist.qty + 1 } : x
          )
        );
        }
        else{
          setCartItems([...cartItems, { ...product, qty: 1 }]);
        }
        
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })
    };

  const onRemove = (product) => {
    const config = {headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json',
    }}

      axios.post('https://joestar-mushroom-farm.herokuapp.com/increment-stock', {
        name: product.name
      }, config)
      .then((res) => {
        let res_body = res.data
        console.log(`incremented ${product.name} stock by ${res_body.removed}`)
        console.log(`Current inventory for ${product.name}: ${res_body.current_stock} `)

        const exist = cartItems.find((x) => x.id === product.id);
        if (exist.qty === 1) {
          setCartItems(cartItems.filter((x) => x.id !== product.id));
        } else {
          setCartItems(
            cartItems.map((x) =>
              x.id === product.id ? { ...exist, qty: exist.qty - 1 } : x
            )
          );
        }

      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })
  };
  return (
    <div className="App">
      <Header countCartItems={cartItems.length}></Header>
      <div className="row">
        <Main products={products} onAdd={onAdd}></Main>
        <Cart
          cartItems={cartItems}
          onAdd={onAdd}
          onRemove={onRemove}
        ></Cart>
      </div>
    </div>
  );
}

export default App;
