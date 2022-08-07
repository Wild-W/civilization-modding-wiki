---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_UPGRADE_RESOURCE_COST_DISCOUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_UPGRADE_RESOURCE_COST_DISCOUNT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>		* The integer percent value of discount on strategic resources required for unit upgrades

## Samples
```SQL {title="PROFESSIONAL_ARMY_UPGRADE_RESOURCE_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PROFESSIONAL_ARMY_UPGRADE_RESOURCE_DISCOUNT",
		"MODIFIER_PLAYER_ADJUST_UNIT_UPGRADE_RESOURCE_COST_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROFESSIONAL_ARMY_UPGRADE_RESOURCE_DISCOUNT",
		"Amount",
		50
	);
	
```

