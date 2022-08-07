---
tags:
- EffectType
title: EFFECT_ADJUST_PLOT_PURCHASE_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLOT_PURCHASE_COST
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="EXPROPRIATION_PLOTPURCHASECOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EXPROPRIATION_PLOTPURCHASECOST",
		"MODIFIER_PLAYER_CITIES_ADJUST_PLOT_PURCHASE_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EXPROPRIATION_PLOTPURCHASECOST",
		"Amount",
		"-20"
	);
	
```

