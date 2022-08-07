---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_SPY_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_SPY_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="LOCAL_INFORMANTS_SPY_DEFENSE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectStackLimit
	)
VALUES
	(
		"LOCAL_INFORMANTS_SPY_DEFENSE_BONUS",
		"MODIFIER_CITY_ADJUST_SPY_BONUS",
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
		"LOCAL_INFORMANTS_SPY_DEFENSE_BONUS",
		"Amount",
		3
	);
	
```

