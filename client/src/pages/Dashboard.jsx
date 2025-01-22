import DBCategories from "../components/DBCategories";
import DBProducts from "../components/DBProducts";
import DBOrders from "../components/DBOrders";

function Dashboard() {
  return (
    <div className="container">
      <div className="db_component">
        <header>
          <div className="logo">
            <span>DBB</span>oard
          </div>
        </header>
      </div>

      <div className="comps">
        <DBCategories />
        <DBProducts />
        <DBOrders />
      </div>
    </div>
  );
}

export default Dashboard;