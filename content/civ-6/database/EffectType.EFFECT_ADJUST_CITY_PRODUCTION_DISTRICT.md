---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_PRODUCTION_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_PRODUCTION_DISTRICT
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MINOR_CIV_INDUSTRIAL_DISTRICT_PRODUCTION_FOR_CAPITAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_INDUSTRIAL_DISTRICT_PRODUCTION_FOR_CAPITAL",
		"MODIFIER_PLAYER_CAPITAL_CITY_ADJUST_DISTRICT_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_INDUSTRIAL_DISTRICT_PRODUCTION_FOR_CAPITAL",
		"Amount",
		2
	);
	
```

