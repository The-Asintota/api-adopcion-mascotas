import { Link } from "react-router-dom";

const Page404 = () => {
    return (
        <main style={{
            display: "grid",
            placeItems: "center",
            height: "100vh",
            textAlign: "center",
            backgroundColor: "var(--green)",
            color: "white"
        }}>
            <div>
                <h1>404</h1>
                <p>Page not found</p>
                <Link to="/">Go to home</Link>
            </div>
        </main>
    );
}

export default Page404;