

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Table `HomeCare`.`dispositivo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HomeCare`.`dispositivo` (
  `imei` INT NOT NULL,
  `data_fabricacao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`imei`),
  UNIQUE INDEX `imei_UNIQUE` (`imei` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `HomeCare`.`erro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HomeCare`.`erro` (
  `id_erro` INT NOT NULL AUTO_INCREMENT,
  `tipo_erro` VARCHAR(45) NOT NULL,
  `fk_dispositivo_erro` INT NOT NULL,
  `data_erro` DATETIME NOT NULL,
  PRIMARY KEY (`id_erro`),
  UNIQUE INDEX `id_erro_UNIQUE` (`id_erro` ASC) VISIBLE,
  CONSTRAINT `erro_disp`
    FOREIGN KEY (`fk_dispositivo_erro`)
    REFERENCES `HomeCare`.`dispositivo` (`imei`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `HomeCare`.`mensagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HomeCare`.`mensagem` (
  `id_mensagem` INT NOT NULL AUTO_INCREMENT,
  `tipo_mensagem` VARCHAR(45) NOT NULL,
  `fk_dispositivo_mensagem` INT NOT NULL,
  `data_mensagem` DATETIME NOT NULL,
  PRIMARY KEY (`id_mensagem`),
  INDEX `mensagem_disp_idx` (`fk_dispositivo_mensagem` ASC) VISIBLE,
  UNIQUE INDEX `id_mensagem_UNIQUE` (`id_mensagem` ASC) VISIBLE,
  CONSTRAINT `mensagem_disp`
    FOREIGN KEY (`fk_dispositivo_mensagem`)
    REFERENCES `HomeCare`.`dispositivo` (`imei`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
