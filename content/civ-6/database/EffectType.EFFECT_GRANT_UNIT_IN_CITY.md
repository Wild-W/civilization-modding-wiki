---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* AllowUniqueOverride `Boolean`
>		* Whether or not to override with unique units
>	* Amount `Integer`
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="UNIQUE_LEADER_ADD_SPY_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent,
		OwnerRequirementSetId
	)
VALUES
	(
		"UNIQUE_LEADER_ADD_SPY_UNIT",
		"MODIFIER_PLAYER_GRANT_UNIT_IN_CAPITAL",
		1,
		1,
		"PLAYER_HAS_CASTLES_TECHNOLOGY_AND_CAPITAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIQUE_LEADER_ADD_SPY_UNIT",
		"AllowUniqueOverride",
		0
	),
	(
		"UNIQUE_LEADER_ADD_SPY_UNIT",
		"Amount",
		1
	),
	(
		"UNIQUE_LEADER_ADD_SPY_UNIT",
		"UnitType",
		"UNIT_SPY"
	);
	
```


```SQL {title="COLOSSUS_GRANT_TRADER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"COLOSSUS_GRANT_TRADER",
		"MODIFIER_SINGLE_CITY_GRANT_UNIT_IN_CITY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COLOSSUS_GRANT_TRADER",
		"Amount",
		1
	),
	(
		"COLOSSUS_GRANT_TRADER",
		"UnitType",
		"UNIT_TRADER"
	);
	
```

