IP=$(cat ./ip.txt)

cat <<EOF >./next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    BACKEND_HOST: "$IP",
  },
};

export default nextConfig;
EOF
