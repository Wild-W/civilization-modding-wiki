---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_GOLD_FROM_CITIZENS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_GOLD_FROM_CITIZENS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TAX_COLLECTOR_ADJUST_CITIZEN_GPT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TAX_COLLECTOR_ADJUST_CITIZEN_GPT",
		"MODIFIER_CITY_ADJUST_CITIZEN_GOLD_PER_TURN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TAX_COLLECTOR_ADJUST_CITIZEN_GPT",
		"Amount",
		2
	);
	
```

