---
tags:
- EffectType
title: EFFECT_ATTACH_MODIFIER_TO_MINORCIVBONUSTYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ATTACH_MODIFIER_TO_MINORCIVBONUSTYPE
>
> * Class: `ANY`
> * Parameters:
>	* ModifierId `String`

## Samples

```SQL {title="APPLY_DISABLE_UNIQUE_SUZERAIN_BONUS_TO_MINORCIVTYPES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APPLY_DISABLE_UNIQUE_SUZERAIN_BONUS_TO_MINORCIVTYPES",
		"MODIFIER_CONGRESS_ATTACH_MODIFIER_TO_MINORCIVBONUSTYPE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APPLY_DISABLE_UNIQUE_SUZERAIN_BONUS_TO_MINORCIVTYPES",
		"ModifierId",
		"WC_RES_DISABLE_UNIQUE_SUZERAIN_BONUS"
	);
	
```

