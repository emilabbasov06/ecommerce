import { useState, useEffect } from "react";

import DBCategories from "../components/DBCategories";
import DBProducts from "../components/DBProducts";
import DBOrders from "../components/DBOrders";

function Dashboard() {
  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const categoriesResponse = await fetch("http://localhost:8000/categories");
        const categoriesData = await categoriesResponse.json();
        setCategories(categoriesData.categories);

        const productsResponse = await fetch("http://localhost:8000/products");
        const productsData = await productsResponse.json();
        setProducts(productsData.products);

        const ordersResponse = await fetch("http://localhost:8000/orders");
        const ordersData = await ordersResponse.json();
        setOrders(ordersData.orders);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  // useEffect(() => {
  //   // Fetch data from the FastAPI backend
  //   fetch("http://localhost:8000/categories")
  //     .then((response) => response.json())
  //     .then((data) => setCategories(data.categories))
  //     .catch((error) => console.error("Error fetching categories:", error));
  // }, []);

  // useEffect(() => {
  //   // Fetch data from the FastAPI backend
  //   fetch("http://localhost:8000/products")
  //     .then((response) => response.json())
  //     .then((data) => setProducts(data.products))
  //     .catch((error) => console.error("Error fetching products:", error));
  // }, []);

  // useEffect(() => {
  //   // Fetch data from the FastAPI backend
  //   fetch("http://localhost:8000/orders")
  //     .then((response) => response.json())
  //     .then((data) => setOrders(data.orders))
  //     .catch((error) => console.error("Error fetching orders:", error));
  // }, []);


  return (
    <div className="container">
      <div className="db_component">
        <header>
          <div className="logo">
            <span>DBB</span>oard
          </div>

          <div className="logout">
            <button>Log out</button>
          </div>
        </header>
      </div>

      <div className="comps">
        <DBCategories categories={categories} />
        <DBProducts products={products} />
        <DBOrders orders={orders} />
      </div>
    </div>
  );
}

export default Dashboard;