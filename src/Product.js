const Cart = ({ cart, removeItem }) => {
    const getCartInfo = () => {
      var totalPrice = 0;
      var buttonStyle = {
        float: "right",
        cursor: "pointer"
      };
      var cartItems = cart.map((item, i) => {
        totalPrice += item.price;
        return (
          <div key={i}>
            {item.name} {item.price}
            <button style={buttonStyle} onClick={removeItem.bind(this, item.id)}>
              Remove
            </button>
          </div>
        );
      });
      return { totalPrice, cartItems };
    };
  
    const info = getCartInfo();
    var cartStyle = {
      border: "2px solid black",
      background: "lightgrey",
      borderRadius: "10px",
      color: "blue",
      margin: "15px",
      padding: "10px",
      width: "30%"
    };
    return (
      <div style={cartStyle}>
        <h1>My shopping Cart</h1>
        {info.cartItems}
        <h2>Total Price : ${info.totalPrice} </h2>
      </div>
    );
  };
  export default Cart;
  