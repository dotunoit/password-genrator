{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd467428",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "def generate_password(length):\n",
    "    characters = string.ascii_letters + string.digits + string.punctuation\n",
    "    password = ''.join(random.choice(characters) for _ in range(length))\n",
    "    return password\n",
    "\n",
    "def main():\n",
    "    length = int(input(\"Enter the length of the password: \"))\n",
    "    password = generate_password(length)\n",
    "    print(\"Generated Password:\", password)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
