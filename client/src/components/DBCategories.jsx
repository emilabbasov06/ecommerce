function DBCategories({ categories }) {
  return (
    <div className="db_component categories">
      <h2>Categories</h2>
      <table>
        <tr>
          <th>CID</th>
          <th>Category</th>
          <th>Created At</th>
        </tr>

        {categories.map((category) => (
          <tr>
            <td>{category.category_id}</td>
            <td>{category.category_name}</td>
            <td>{category.created_at}</td>
          </tr>
        ))}
      </table>
    </div>
  );
}

export default DBCategories;