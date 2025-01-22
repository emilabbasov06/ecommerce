function DBOrders() {
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
        <tr>
          <td>1</td>
          <td>IPhone 14 Pro</td>
          <td>2025-01-21 22:10:35</td>
          <td><span className="money">1299.89 $</span></td>
        </tr>
      </table>
    </div>
  );
}

export default DBOrders;