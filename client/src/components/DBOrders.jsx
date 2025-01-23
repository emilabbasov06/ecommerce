function DBOrders({ orders }) {
  return (
    <div className="db_component orders">
      <h2>Orders</h2>
      <table>
        <tr>
          <th>OID</th>
          <th>Order</th>
          <th>Date and Time</th>
          <th>Price</th>
        </tr>
        {orders.map((order) => (
          <tr>
            <td>{order.order_id}</td>
            <td>{order.order_name}</td>
            <td>{order.order_date}</td>
            <td>{order.order_price} $</td>
          </tr>
        ))}
      </table>
    </div>
  );
}

export default DBOrders;