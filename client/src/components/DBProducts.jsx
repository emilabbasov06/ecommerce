function DBProducts() {
  return (
    <div className="db_component products">
      <h2>Products</h2>
      <table>
        <tr>
          <th>PID</th>
          <th>Product</th>
          <th>Content</th>
          <th>Price</th>
          <th>Date Added</th>
          <th>Category</th>
        </tr>
        <tr>
          <td>1</td>
          <td>IPhone 14 Pro</td>
          <td>Some phone</td>
          <td><span className="money">1299.89 $</span></td>
          <td>25th January 2024</td>
          <td>Smartphones</td>
        </tr>
      </table>
    </div>
  );
}

export default DBProducts;