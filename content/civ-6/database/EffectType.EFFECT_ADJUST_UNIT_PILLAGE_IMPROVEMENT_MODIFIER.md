---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PILLAGE_IMPROVEMENT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PILLAGE_IMPROVEMENT_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="RAID_DOUBLEPILLAGEIMPROVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RAID_DOUBLEPILLAGEIMPROVE",
		"MODIFIER_PLAYER_ADJUST_IMPROVEMENT_PILLAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value,
		Extra
	)
VALUES
	(
		"RAID_DOUBLEPILLAGEIMPROVE",
		"Amount",
		50,
		"-1"
	);
	
```

