import React from 'react'
import { useEffect } from "react";

const ErrorMessage = ({error}) => {

    useEffect(() => {
        if (error) {
          console.log(error);
        }
      }, [error]);

  return (
    error && <span className="text-red-800 text-sm">{error.message}</span>

  )
}

export default ErrorMessage
