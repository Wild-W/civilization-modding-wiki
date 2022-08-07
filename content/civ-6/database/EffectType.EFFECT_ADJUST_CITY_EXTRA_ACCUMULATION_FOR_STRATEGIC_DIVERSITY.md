---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION_FOR_STRATEGIC_DIVERSITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION_FOR_STRATEGIC_DIVERSITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GRANDBAZAAR_ACCUMULATION_STRATEGICS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GRANDBAZAAR_ACCUMULATION_STRATEGICS",
		"MODIFIER_SINGLE_CITY_ADJUST_EXTRA_ACCUMULATION_FOR_STRATEGIC_DIVERSITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GRANDBAZAAR_ACCUMULATION_STRATEGICS",
		"Amount",
		1
	);
	
```

