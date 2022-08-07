---
tags:
- EffectType
title: EFFECT_ADJUST_GOVERNOR_IDENTITY_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GOVERNOR_IDENTITY_PRESSURE
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Amount `Integer`
>		* The delta amount of pressure to modify the strength.
>	* DomesticCities `Boolean`
>		* If true\, the effect will apply the value to the Governor's external domestic pressure.
>	* ForeignCities `Boolean`
>		* If true\, the effect will apply the value to the Governor's external foreign pressure.
>	* OncePerCity `Unknown`

## Samples

```SQL {title="TOQUI_DOMESTIC_LOYALTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TOQUI_DOMESTIC_LOYALTY",
		"MODIFIER_PLAYER_GOVERNORS_ADJUST_GOVERNOR_IDENTITY_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOQUI_DOMESTIC_LOYALTY",
		"Amount",
		4
	),
	(
		"TOQUI_DOMESTIC_LOYALTY",
		"DomesticCities",
		1
	),
	(
		"TOQUI_DOMESTIC_LOYALTY",
		"OncePerCity",
		1
	);
	
```


```SQL {title="TOQUI_FOREIGN_LOYALTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TOQUI_FOREIGN_LOYALTY",
		"MODIFIER_PLAYER_GOVERNORS_ADJUST_GOVERNOR_IDENTITY_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOQUI_FOREIGN_LOYALTY",
		"Amount",
		4
	),
	(
		"TOQUI_FOREIGN_LOYALTY",
		"ForeignCities",
		1
	),
	(
		"TOQUI_FOREIGN_LOYALTY",
		"OncePerCity",
		1
	);
	
```

