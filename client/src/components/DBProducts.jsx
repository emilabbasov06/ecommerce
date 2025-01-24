function DBProducts({ products }) {
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
        {products.map((product) => (
          <tr>
            <td>{product.product_id}</td>
            <td>{product.product_name}</td>
            <td>{product.content}</td>
            <td>{product.price} $</td>
            <td>{product.created_at}</td>
            <td>{product.category_id}</td>
          </tr>
        ))}
      </table>
    </div>
  );
}

export default DBProducts;