---
tags:
- EffectType
title: EFFECT_ADJUST_CITIES_FRESHWATER_HOUSING_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITIES_FRESHWATER_HOUSING_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* HasBonus `Boolean`

## Samples

```SQL {title="MINOR_CIV_MOHENJO_DARO_CITIES_FRESHWATER_HOUSING_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_MOHENJO_DARO_CITIES_FRESHWATER_HOUSING_BONUS",
		"MODIFIER_PLAYER_GRANT_CITIES_FRESHWATER_HOUSING_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_MOHENJO_DARO_CITIES_FRESHWATER_HOUSING_BONUS",
		"HasBonus",
		1
	);
	
```

