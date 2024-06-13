import argparse
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from prettytable import PrettyTable
from database import OperationsGuard, ManagementGuard, Incident